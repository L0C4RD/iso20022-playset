# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account32
from . import CommunicationAddress6
from . import LEIIdentifier
from . import NameAndAddress4
from . import PartyIdentification177Choice
from . import PartyRole2Choice
from . import YesNoIndicator

class Intermediary46(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Id", "_LglNttyIdr", "_NmAndAdr", "_PmryComAdr", "_Role", "_ScndryComAdr", "_WvdTrlrComssnInd"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', Account32, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', Account32, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification177Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification177Choice, False)

	@property
	def LglNttyIdr(self):
		return self._LglNttyIdr

	@LglNttyIdr.setter
	def LglNttyIdr(self, value):
		self._LglNttyIdr = value if value is not None else base_types.UninitialisedField(self, 'LglNttyIdr', LEIIdentifier, False)

	@LglNttyIdr.deleter
	def LglNttyIdr(self):
		del self._LglNttyIdr
		self._LglNttyIdr = base_types.UninitialisedField(self, 'LglNttyIdr', LEIIdentifier, False)

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress4, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress4, False)

	@property
	def PmryComAdr(self):
		return self._PmryComAdr

	@PmryComAdr.setter
	def PmryComAdr(self, value):
		self._PmryComAdr = value if value is not None else base_types.UninitialisedField(self, 'PmryComAdr', CommunicationAddress6, True)

	@PmryComAdr.deleter
	def PmryComAdr(self):
		del self._PmryComAdr
		self._PmryComAdr = base_types.UninitialisedField(self, 'PmryComAdr', CommunicationAddress6, True)

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if value is not None else base_types.UninitialisedField(self, 'Role', PartyRole2Choice, False)

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = base_types.UninitialisedField(self, 'Role', PartyRole2Choice, False)

	@property
	def ScndryComAdr(self):
		return self._ScndryComAdr

	@ScndryComAdr.setter
	def ScndryComAdr(self, value):
		self._ScndryComAdr = value if value is not None else base_types.UninitialisedField(self, 'ScndryComAdr', CommunicationAddress6, True)

	@ScndryComAdr.deleter
	def ScndryComAdr(self):
		del self._ScndryComAdr
		self._ScndryComAdr = base_types.UninitialisedField(self, 'ScndryComAdr', CommunicationAddress6, True)

	@property
	def WvdTrlrComssnInd(self):
		return self._WvdTrlrComssnInd

	@WvdTrlrComssnInd.setter
	def WvdTrlrComssnInd(self, value):
		self._WvdTrlrComssnInd = value if value is not None else base_types.UninitialisedField(self, 'WvdTrlrComssnInd', YesNoIndicator, False)

	@WvdTrlrComssnInd.deleter
	def WvdTrlrComssnInd(self):
		del self._WvdTrlrComssnInd
		self._WvdTrlrComssnInd = base_types.UninitialisedField(self, 'WvdTrlrComssnInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=Account32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification177Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryComAdr', type=CommunicationAddress6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Role', type=PartyRole2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryComAdr', type=CommunicationAddress6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WvdTrlrComssnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))