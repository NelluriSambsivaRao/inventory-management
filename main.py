import item
import customer
import supplier
import transaction
import report
import os
while(True):
    os.system('cls')
    print("="*80)
    print("-"*80)
    print("\n\t\t\tInventory Management System\n")
    print("-"*80)
    print("="*80)
    print("\n\t\t\t\tEnter your choice\n\t\t\t\t1.Items\n\t\t\t\
     \t2.Customers\n\t\t\t\t3.Suppliers\
     \n\t\t\t\t4.Transaction\n\t\t\t\t5.Report\n\t\t\t\t6.Exit")
    ch=int(input())
    if ch==1:
        while(True):
            print("---------------\nEnter your choice\n--------------\
 \n\t\t\t\t1.Add Item\n\t\t\t\t2.Edit Item\n\t\t\t\t3.Fix Rate\
 \n\t\t\t\t4.Search Item\n\t\t\t\t5.Delete Item\n\t\t\t\t6.Exit")
            ch=int(input())
            if ch==1:
                item.add_item()
            elif ch==2:
                item.edit_item()
            elif ch==3:
                item.fix_rate()
            elif ch==4:
                item.search_item()
            elif ch==5:
                item.delete_item()
            elif ch==6:
                break
    elif ch==2:
        while(True):
            print("\n---------------\nEnter your choice\n--------------\
 \n\t\t\t\t1.Add customers\n\t\t\t\t2.Edit Customers\
 \n\t\t\t\t3.Search Customers\n\t\t\t\t4.Delete Customers\n\t\t\t\t5.exit")
            ch=int(input())
            if ch==1:
                customer.add_customer()
            elif ch==2:
                customer.edit_customer()
            elif ch==3:
                customer.search_customer()
            elif ch==4:
                customer.delete_customer()
            elif ch==5:
                break
    elif ch==3:
        while(True):
            print("\n---------------\nEnter your choice\n--------------\
 \n\t\t\t\t1.Add Suppliers\n\t\t\t\t2.Edit Suppliers\
 \n\t\t\t\t3.Search Suppliers\n\t\t\t\t4.Delete Suppliers\n\t\t\t\t5.exit")
            ch=int(input())
            if ch==1:
                supplier.add_supplier()
            elif ch==2:
                supplier.edit_supplier()
            elif ch==3:
                supplier.search_supplier()
            elif ch==4:
                supplier.delete_supplier()
            elif ch==5:
                break
    elif ch==4:
        while(True):
            print("\n---------------\nEnter your choice\n--------------\
 \n\t\t\t\t1.Sale\n\t\t\t\t2.Purchase\n\t\t\t\t3.exit")
            ch=int(input())
            if ch==1:
                transaction.sale()
            elif ch==2:
                transaction.purchase()
            elif ch==3:
                break
    elif ch==5:
        while(True):
            print("\n---------------\nEnter your choice\n--------------\
 \n\t\t\t\t1.Item Details\n\t\t\t\t2.Customer Details\
 \n\t\t\t\t3.Supplier Details\n\t\t\t\t4.Sale Details\n\
 \t\t\t5.Purchase Details\n\t\t\t\t6.Best Selling Product(Plot)\
 \n\t\t\t\t7.Sale Performance(Plot)\n\t\t\t\t8.exit")
            ch=int(input())
            if ch==1:
                report.show_item()
            elif ch==2:
                report.show_customer()
            elif ch==3:
                report.show_supplier()
            elif ch==4:
                report.show_sale()
            elif ch==5:
                report.show_purchase()
            elif ch==6:
                report.best_product()
            elif ch==7:
                report.sale_performance()
            elif ch==8:
                break
    elif ch==6:
        break
    
 
