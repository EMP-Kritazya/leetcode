class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction_dicts = {}
        invalid_transactions = []

        for i in transactions:
            split_text = i.split(',')
            if int(split_text[2]) >= 1000:
                invalid_transactions.append(i)
                continue

            elif split_text[0] in transaction_dicts:
                isValid = True
                
                # # Filtering duplicate transaction first:
                # if i in transaction_dicts[split_text[0]]:
                #     continue
    
                for j in transaction_dicts[split_text[0]]:
                    stored_items = j.split(',')
                    
                    # if only time difference is less than 60 we omit the next transaction
                    # but if the city changes then we need to discard previous as well as current transaction
                    if 0<abs(int(split_text[1])-int(stored_items[1]))<= 60 and stored_items[3] != split_text[3]:        
                        isValid = False
                        invalid_transactions.append(j)
                        invalid_transactions.append(i)
                        transaction_dicts[split_text[0]].remove(j)
                        continue
                    if 0<abs(int(split_text[1])-int(stored_items[1])) <= 60 and stored_items[3] == split_text[3]:
                        isValid = False
                        invalid_transactions.append(i)
                        continue
                      
                if isValid:
                    transaction_dicts[split_text[0]].append(i)
            
            else:
                transaction_dicts[split_text[0]] = [i]

        return invalid_transactions


