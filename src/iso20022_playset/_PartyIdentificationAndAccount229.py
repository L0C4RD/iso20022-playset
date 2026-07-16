# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactIdentification2
from . import DateAndDateTime2Choice
from . import Max35Text
from . import PartyIdentification254Choice
from . import SubAccount4

class PartyIdentificationAndAccount229(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_CtctPrsn", "_PrcgDt", "_PrcgId", "_PtyId", "_SubAcct"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'CtctPrsn', ContactIdentification2, False)

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = base_types.UninitialisedField(self, 'CtctPrsn', ContactIdentification2, False)

	@property
	def PrcgDt(self):
		return self._PrcgDt

	@PrcgDt.setter
	def PrcgDt(self, value):
		self._PrcgDt = value if value is not None else base_types.UninitialisedField(self, 'PrcgDt', DateAndDateTime2Choice, False)

	@PrcgDt.deleter
	def PrcgDt(self):
		del self._PrcgDt
		self._PrcgDt = base_types.UninitialisedField(self, 'PrcgDt', DateAndDateTime2Choice, False)

	@property
	def PrcgId(self):
		return self._PrcgId

	@PrcgId.setter
	def PrcgId(self, value):
		self._PrcgId = value if value is not None else base_types.UninitialisedField(self, 'PrcgId', Max35Text, False)

	@PrcgId.deleter
	def PrcgId(self):
		del self._PrcgId
		self._PrcgId = base_types.UninitialisedField(self, 'PrcgId', Max35Text, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification254Choice, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification254Choice, False)

	@property
	def SubAcct(self):
		return self._SubAcct

	@SubAcct.setter
	def SubAcct(self, value):
		self._SubAcct = value if value is not None else base_types.UninitialisedField(self, 'SubAcct', SubAccount4, False)

	@SubAcct.deleter
	def SubAcct(self):
		del self._SubAcct
		self._SubAcct = base_types.UninitialisedField(self, 'SubAcct', SubAccount4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification254Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcct', type=SubAccount4, min=0, max=1, mutex_group=None, array=False),
	))