def breakingRecords(scores):
    
    records_broken = [0, 0]
    max_record = scores[0]
    min_record = scores[0]

    for score in scores:
        if score > max_record:
            max_record = score
            records_broken[0] += 1
        elif score < min_record:
            min_record = score
            records_broken[1] += 1

    return records_broken