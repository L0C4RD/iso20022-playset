# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from ._ISODate import ISODate

class SubscriptionInformation2(base_types._BaseFieldType):

	__slots__ = ["_CshCmpnt", "_DtOfFrstSbcpt", "_EqtyCmpnt", "_TtlAmtYrToDt"]
	@property
	def CshCmpnt(self):
		return self._CshCmpnt

	@CshCmpnt.setter
	def CshCmpnt(self, value):
		self._CshCmpnt = value if type(value) != base_types.auto else self.make_default("CshCmpnt")

	@CshCmpnt.deleter
	def CshCmpnt(self):
		del self._CshCmpnt
		self._CshCmpnt = None

	@property
	def DtOfFrstSbcpt(self):
		return self._DtOfFrstSbcpt

	@DtOfFrstSbcpt.setter
	def DtOfFrstSbcpt(self, value):
		self._DtOfFrstSbcpt = value if type(value) != base_types.auto else self.make_default("DtOfFrstSbcpt")

	@DtOfFrstSbcpt.deleter
	def DtOfFrstSbcpt(self):
		del self._DtOfFrstSbcpt
		self._DtOfFrstSbcpt = None

	@property
	def EqtyCmpnt(self):
		return self._EqtyCmpnt

	@EqtyCmpnt.setter
	def EqtyCmpnt(self, value):
		self._EqtyCmpnt = value if type(value) != base_types.auto else self.make_default("EqtyCmpnt")

	@EqtyCmpnt.deleter
	def EqtyCmpnt(self):
		del self._EqtyCmpnt
		self._EqtyCmpnt = None

	@property
	def TtlAmtYrToDt(self):
		return self._TtlAmtYrToDt

	@TtlAmtYrToDt.setter
	def TtlAmtYrToDt(self, value):
		self._TtlAmtYrToDt = value if type(value) != base_types.auto else self.make_default("TtlAmtYrToDt")

	@TtlAmtYrToDt.deleter
	def TtlAmtYrToDt(self):
		del self._TtlAmtYrToDt
		self._TtlAmtYrToDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshCmpnt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfFrstSbcpt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqtyCmpnt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtYrToDt', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
	))