# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import BICIdentifier
from . import CashAccountIdentification1Choice
from . import PartyIdentification2Choice

class CashAccount17(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnrId", "_CrspdtBkId", "_PmtCcy"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', CashAccountIdentification1Choice, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', CashAccountIdentification1Choice, False)

	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrId', PartyIdentification2Choice, False)

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = base_types.UninitialisedField(self, 'AcctOwnrId', PartyIdentification2Choice, False)

	@property
	def CrspdtBkId(self):
		return self._CrspdtBkId

	@CrspdtBkId.setter
	def CrspdtBkId(self, value):
		self._CrspdtBkId = value if value is not None else base_types.UninitialisedField(self, 'CrspdtBkId', BICIdentifier, False)

	@CrspdtBkId.deleter
	def CrspdtBkId(self):
		del self._CrspdtBkId
		self._CrspdtBkId = base_types.UninitialisedField(self, 'CrspdtBkId', BICIdentifier, False)

	@property
	def PmtCcy(self):
		return self._PmtCcy

	@PmtCcy.setter
	def PmtCcy(self, value):
		self._PmtCcy = value if value is not None else base_types.UninitialisedField(self, 'PmtCcy', ActiveCurrencyCode, False)

	@PmtCcy.deleter
	def PmtCcy(self):
		del self._PmtCcy
		self._PmtCcy = base_types.UninitialisedField(self, 'PmtCcy', ActiveCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=CashAccountIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrspdtBkId', type=BICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))