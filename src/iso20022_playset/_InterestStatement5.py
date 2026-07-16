# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import DatePeriod2
from . import ISODate
from . import InterestCalculation5
from . import Max35Text

class InterestStatement5(base_types._BaseFieldType):

	__slots__ = ["_IntrstClctn", "_IntrstPmtReqId", "_IntrstPrd", "_TtlIntrstAmtDueToA", "_TtlIntrstAmtDueToB", "_ValDt"]
	@property
	def IntrstClctn(self):
		return self._IntrstClctn

	@IntrstClctn.setter
	def IntrstClctn(self, value):
		self._IntrstClctn = value if value is not None else base_types.UninitialisedField(self, 'IntrstClctn', InterestCalculation5, True)

	@IntrstClctn.deleter
	def IntrstClctn(self):
		del self._IntrstClctn
		self._IntrstClctn = base_types.UninitialisedField(self, 'IntrstClctn', InterestCalculation5, True)

	@property
	def IntrstPmtReqId(self):
		return self._IntrstPmtReqId

	@IntrstPmtReqId.setter
	def IntrstPmtReqId(self, value):
		self._IntrstPmtReqId = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtReqId', Max35Text, False)

	@IntrstPmtReqId.deleter
	def IntrstPmtReqId(self):
		del self._IntrstPmtReqId
		self._IntrstPmtReqId = base_types.UninitialisedField(self, 'IntrstPmtReqId', Max35Text, False)

	@property
	def IntrstPrd(self):
		return self._IntrstPrd

	@IntrstPrd.setter
	def IntrstPrd(self, value):
		self._IntrstPrd = value if value is not None else base_types.UninitialisedField(self, 'IntrstPrd', DatePeriod2, False)

	@IntrstPrd.deleter
	def IntrstPrd(self):
		del self._IntrstPrd
		self._IntrstPrd = base_types.UninitialisedField(self, 'IntrstPrd', DatePeriod2, False)

	@property
	def TtlIntrstAmtDueToA(self):
		return self._TtlIntrstAmtDueToA

	@TtlIntrstAmtDueToA.setter
	def TtlIntrstAmtDueToA(self, value):
		self._TtlIntrstAmtDueToA = value if value is not None else base_types.UninitialisedField(self, 'TtlIntrstAmtDueToA', ActiveCurrencyAndAmount, False)

	@TtlIntrstAmtDueToA.deleter
	def TtlIntrstAmtDueToA(self):
		del self._TtlIntrstAmtDueToA
		self._TtlIntrstAmtDueToA = base_types.UninitialisedField(self, 'TtlIntrstAmtDueToA', ActiveCurrencyAndAmount, False)

	@property
	def TtlIntrstAmtDueToB(self):
		return self._TtlIntrstAmtDueToB

	@TtlIntrstAmtDueToB.setter
	def TtlIntrstAmtDueToB(self, value):
		self._TtlIntrstAmtDueToB = value if value is not None else base_types.UninitialisedField(self, 'TtlIntrstAmtDueToB', ActiveCurrencyAndAmount, False)

	@TtlIntrstAmtDueToB.deleter
	def TtlIntrstAmtDueToB(self):
		del self._TtlIntrstAmtDueToB
		self._TtlIntrstAmtDueToB = base_types.UninitialisedField(self, 'TtlIntrstAmtDueToB', ActiveCurrencyAndAmount, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstClctn', type=InterestCalculation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstPmtReqId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPrd', type=DatePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlIntrstAmtDueToA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlIntrstAmtDueToB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))