// event_emitter_2694.js


class EventEmitter {

    constructor() {
        this.events = {};
    }


    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {

        if (!this.events[eventName]) {
            this.events[eventName] = [];
        }

        this.events[eventName].push(callback);

        return {
            unsubscribe: () => {
                this.events[eventName] = this.events[eventName].filter(f => f !== callback);
                if (this.events[eventName].length === 0) {
                    delete this.events[eventName];
                }

            }
        };
    }

    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        if (!this.events[eventName]) {
            return [];
        }

        return this.events[eventName].map(callback => callback(...args));
    }
}


const emitter = new EventEmitter();

// Subscribe to an event
const sub = emitter.subscribe('data', (x) => x * 2);
const sub2 = emitter.subscribe('data', (x) => x + 3);

// Emit the event and pass arguments
console.log(emitter.emit('data', [5])); // Output: [10, 8]

// Unsubscribe from the first event listener
sub.unsubscribe();

// Emit the event again
console.log(emitter.emit('data', [5])); // Output: [8]
