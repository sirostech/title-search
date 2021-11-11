import { writable } from 'svelte/store';

export const search_results = writable([]);

export const active_result = writable(-1);
