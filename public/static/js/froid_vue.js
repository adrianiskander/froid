'use strict';


let config = {
  apiUrl: '/api'
};


let getRandInt = function(min, max) {
  /*
    Return random integer.
  */
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
};


let scrollDown = function() {
  /*
    Scroll to bottom of the page.
  */
  window.setTimeout(function() {
    window.scrollTo(0, document.body.scrollHeight);
  }, 1);
};


let app = new Vue({

  el: '#app',

  data: {
    messages: []
  },

  created: function() {

    let messages = JSON.parse(window.sessionStorage.getItem('messages'));

    if (messages) {
      this.messages = messages;
      scrollDown();
    }
  },

  methods: {
    requestGetGreeting: function() {
      /*
        Get greeting from agent.
      */
      let req = new XMLHttpRequest();
      let self = this;      

      req.open('GET', config.apiUrl + '/greeting');
      req.send(null);
      req.onload = function() {
        if (req.status === 200) {
          self.pushMessage(req.response);
        }
      }
    },

    requestPostMessage: function(message) {
      /*
        Post message/stimulus to agent.
      */
      let req = new XMLHttpRequest();
      let self = this;      

      req.open('POST', config.apiUrl + '/stimulus');
      req.send(message);
      req.onload = function() {
        if (req.status === 200) {
          self.pushMessage(req.response);
        }
      }
    },

    pushMessage: function(message) {
      /*
        Push message to app messages with little delay to simulate homan.
      */
      let self = this;

      window.setTimeout(function() {
        self.messages.push(message);
        window.sessionStorage.setItem('messages', JSON.stringify(self.messages));
        scrollDown();
      }, getRandInt(3, 5) * 1000);
    },

    submitMessage: function(event) {
      event.preventDefault();

      let message = event.target.message.value;

      if ( ! message) { return; };
      
      this.messages.push(message);
      this.requestPostMessage(message);
      event.target.message.value = '';
      scrollDown();
    }
  }
});


window.addEventListener('resize', function() {
  scrollDown();
});


window.setTimeout(function() {
  /*
    Say hello first if user is not writing anything.
  */
  if (app.messages.length < 1) {
    app.requestGetGreeting();
  }
}, getRandInt(10000, 15000));
