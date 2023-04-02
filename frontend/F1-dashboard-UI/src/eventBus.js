import { reactive } from 'vue';

export const EventBus = reactive({
  callbacks: {},
  $on(event, callback) {
    if (!this.callbacks[event]) {
      this.callbacks[event] = [];
    }
    this.callbacks[event].push(callback);
  },
  $emit(event, payload) {
    if (this.callbacks[event]) {
      this.callbacks[event].forEach(callback => callback(payload));
    }
  },
});