import { observable, computed, action } from 'mobx';
import { VoterService, IncomingRegistrationJSON } from './voter-service';

export class Voter {
  @observable firstName: string
  @observable lastName: string
  @observable birthDate: string
  @observable zipCode: string
  @observable registered: boolean

  @action
  checkRegistration() {
    return VoterService.checkRegistration(this.firstName, this.lastName, this.birthDate, this.zipCode).then(
      result => Object.assign(this, result)
    );
  }
}