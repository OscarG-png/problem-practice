function selectionSort(items) {
    const length = items.length;
    for (let i = 0; i < length; i++) {
        let min = i;
        for (let j = i + 1; j < length; j++) {
            if (items[j] < items[min]) {
                min = j;
            }
        }
        if (min !== i) {
            const temp = items[i];
            items[i] = items[min];
            items[min] = temp;
        }
    }
    return items;
}
