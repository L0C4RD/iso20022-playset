# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CashCollateral5
from . import Max1025Text

class ContractCollateral1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CollDesc", "_TtlAmt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@property
	def CollDesc(self):
		return self._CollDesc

	@CollDesc.setter
	def CollDesc(self, value):
		self._CollDesc = value if value is not None else base_types.UninitialisedField(self, 'CollDesc', CashCollateral5, True)

	@CollDesc.deleter
	def CollDesc(self):
		del self._CollDesc
		self._CollDesc = base_types.UninitialisedField(self, 'CollDesc', CashCollateral5, True)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ActiveCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollDesc', type=CashCollateral5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))