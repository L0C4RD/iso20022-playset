# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import ISODate
from . import Max35Text
from . import UUIDv4Identifier

class ShortPaymentIdentification4(base_types._BaseFieldType):

	__slots__ = ["_InstgAgt", "_IntrBkSttlmDt", "_TxId", "_UETR"]
	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if value is not None else base_types.UninitialisedField(self, 'InstgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = base_types.UninitialisedField(self, 'InstgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, False)

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@property
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if value is not None else base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, False)

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))