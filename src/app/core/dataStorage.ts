//  ===========================================================================================================
// Original Author : Ashwini Lamsoge
// Creation Date   : 27/02/2021
// Project Name    : Berar Finance
// Module Name	   : Core
// Name            : DataStorage 

// Modify Author    -   Modify Date   -  Reason Of Modify

// Akshay  B         -   19/01/2021    - Added properties to store session data.
// Akshay  B         -   10/02/2021    - changed login user type name and data type to login user details and any.
// Ashwini L         -   03/04/2021    - create New 

// ==================================================================================================================================
import { Injectable } from '@angular/core';
import { Time } from '@angular/common';

@Injectable()
export class DataStorage {
    public data: any;
    /**
     * get and set login user type
     */
    private _loginUserDetails: any
    get loginUserDetails(): any {
        return this._loginUserDetails;
    }
    set loginUserDetails(value) {
        this._loginUserDetails = value;
    }
    /**
     * get and set login user info
     */
    private _logInfo: any;
    get logInfo(): any {
        return this._logInfo;
    }
    set logInfo(value) {
        this._logInfo = value;
    }

    private _sessionValue: any;
    get sessionValue(): any {
        return this._sessionValue;
    }
    set sessionValue(value) {
        this._sessionValue = value;
    }

    private _childMenuInfo: any;
    get childMenuInfo(): any {
        return this._childMenuInfo;
    }
    
    set childMenuInfo(value) {
        this._childMenuInfo = value;
    }

    private _shortMenu: any;
    get shortMenu(): any {
        return this._shortMenu;
    }
    
    set shortMenu(value) {
        this._shortMenu = value;
    }

    private _userRemainder: any;
    get userRemainder(): any {
        return this._userRemainder;
    }
    
    set userRemainder(value) {
        this._userRemainder = value;
    }
    public constructor() {

    }
}

