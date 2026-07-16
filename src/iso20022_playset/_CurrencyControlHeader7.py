# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import ISODateTime
from . import Max15NumericText
from . import Max35Text
from . import PartyIdentification272

class CurrencyControlHeader7(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_MsgId", "_NbOfItms", "_RcvgPty", "_RegnAgt"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def NbOfItms(self):
		return self._NbOfItms

	@NbOfItms.setter
	def NbOfItms(self, value):
		self._NbOfItms = value if value is not None else base_types.UninitialisedField(self, 'NbOfItms', Max15NumericText, False)

	@NbOfItms.deleter
	def NbOfItms(self):
		del self._NbOfItms
		self._NbOfItms = base_types.UninitialisedField(self, 'NbOfItms', Max15NumericText, False)

	@property
	def RcvgPty(self):
		return self._RcvgPty

	@RcvgPty.setter
	def RcvgPty(self, value):
		self._RcvgPty = value if value is not None else base_types.UninitialisedField(self, 'RcvgPty', PartyIdentification272, False)

	@RcvgPty.deleter
	def RcvgPty(self):
		del self._RcvgPty
		self._RcvgPty = base_types.UninitialisedField(self, 'RcvgPty', PartyIdentification272, False)

	@property
	def RegnAgt(self):
		return self._RegnAgt

	@RegnAgt.setter
	def RegnAgt(self, value):
		self._RegnAgt = value if value is not None else base_types.UninitialisedField(self, 'RegnAgt', BranchAndFinancialInstitutionIdentification8, False)

	@RegnAgt.deleter
	def RegnAgt(self):
		del self._RegnAgt
		self._RegnAgt = base_types.UninitialisedField(self, 'RegnAgt', BranchAndFinancialInstitutionIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfItms', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgPty', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
	))