# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentificationFormatChoice
from . import Intermediary11
from . import Max35Text
from . import PartyIdentification2Choice
from . import YesNoIndicator

class SafekeepingAccount2(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AcctSvcr", "_Dsgnt", "_FngbInd", "_Id", "_IntrmyInf", "_Nm"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification2Choice, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification2Choice, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification2Choice, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification2Choice, False)

	@property
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if value is not None else base_types.UninitialisedField(self, 'Dsgnt', Max35Text, False)

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = base_types.UninitialisedField(self, 'Dsgnt', Max35Text, False)

	@property
	def FngbInd(self):
		return self._FngbInd

	@FngbInd.setter
	def FngbInd(self, value):
		self._FngbInd = value if value is not None else base_types.UninitialisedField(self, 'FngbInd', YesNoIndicator, False)

	@FngbInd.deleter
	def FngbInd(self):
		del self._FngbInd
		self._FngbInd = base_types.UninitialisedField(self, 'FngbInd', YesNoIndicator, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', AccountIdentificationFormatChoice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', AccountIdentificationFormatChoice, False)

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if value is not None else base_types.UninitialisedField(self, 'IntrmyInf', Intermediary11, True)

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = base_types.UninitialisedField(self, 'IntrmyInf', Intermediary11, True)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FngbInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AccountIdentificationFormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary11, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))