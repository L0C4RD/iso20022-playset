# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDepositedMedia4
from . import CardAccount21
from . import ContentInformationType10
from . import DetailedAmount16
from . import Max70Text

class ATMDepositComponent1(base_types._BaseFieldType):

	__slots__ = ["_AcctData", "_DpstdMdia", "_DtldReqdAmt", "_PrtctdAcctData", "_SubDpstId"]
	@property
	def AcctData(self):
		return self._AcctData

	@AcctData.setter
	def AcctData(self, value):
		self._AcctData = value if value is not None else base_types.UninitialisedField(self, 'AcctData', CardAccount21, True)

	@AcctData.deleter
	def AcctData(self):
		del self._AcctData
		self._AcctData = base_types.UninitialisedField(self, 'AcctData', CardAccount21, True)

	@property
	def DpstdMdia(self):
		return self._DpstdMdia

	@DpstdMdia.setter
	def DpstdMdia(self, value):
		self._DpstdMdia = value if value is not None else base_types.UninitialisedField(self, 'DpstdMdia', ATMDepositedMedia4, True)

	@DpstdMdia.deleter
	def DpstdMdia(self):
		del self._DpstdMdia
		self._DpstdMdia = base_types.UninitialisedField(self, 'DpstdMdia', ATMDepositedMedia4, True)

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount16, True)

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount16, True)

	@property
	def PrtctdAcctData(self):
		return self._PrtctdAcctData

	@PrtctdAcctData.setter
	def PrtctdAcctData(self, value):
		self._PrtctdAcctData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdAcctData', ContentInformationType10, True)

	@PrtctdAcctData.deleter
	def PrtctdAcctData(self):
		del self._PrtctdAcctData
		self._PrtctdAcctData = base_types.UninitialisedField(self, 'PrtctdAcctData', ContentInformationType10, True)

	@property
	def SubDpstId(self):
		return self._SubDpstId

	@SubDpstId.setter
	def SubDpstId(self, value):
		self._SubDpstId = value if value is not None else base_types.UninitialisedField(self, 'SubDpstId', Max70Text, False)

	@SubDpstId.deleter
	def SubDpstId(self):
		del self._SubDpstId
		self._SubDpstId = base_types.UninitialisedField(self, 'SubDpstId', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctData', type=CardAccount21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DpstdMdia', type=ATMDepositedMedia4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdAcctData', type=ContentInformationType10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubDpstId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))