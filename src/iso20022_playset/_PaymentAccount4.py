# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AmountAndDirection86
from . import ImpliedCurrencyAndAmount
from . import Max10NumericText

class PaymentAccount4(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_GrssCdts", "_GrssDbts", "_LatePmtConf", "_NetPmt"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def GrssCdts(self):
		return self._GrssCdts

	@GrssCdts.setter
	def GrssCdts(self, value):
		self._GrssCdts = value if value is not None else base_types.UninitialisedField(self, 'GrssCdts', ImpliedCurrencyAndAmount, False)

	@GrssCdts.deleter
	def GrssCdts(self):
		del self._GrssCdts
		self._GrssCdts = base_types.UninitialisedField(self, 'GrssCdts', ImpliedCurrencyAndAmount, False)

	@property
	def GrssDbts(self):
		return self._GrssDbts

	@GrssDbts.setter
	def GrssDbts(self, value):
		self._GrssDbts = value if value is not None else base_types.UninitialisedField(self, 'GrssDbts', ImpliedCurrencyAndAmount, False)

	@GrssDbts.deleter
	def GrssDbts(self):
		del self._GrssDbts
		self._GrssDbts = base_types.UninitialisedField(self, 'GrssDbts', ImpliedCurrencyAndAmount, False)

	@property
	def LatePmtConf(self):
		return self._LatePmtConf

	@LatePmtConf.setter
	def LatePmtConf(self, value):
		self._LatePmtConf = value if value is not None else base_types.UninitialisedField(self, 'LatePmtConf', Max10NumericText, False)

	@LatePmtConf.deleter
	def LatePmtConf(self):
		del self._LatePmtConf
		self._LatePmtConf = base_types.UninitialisedField(self, 'LatePmtConf', Max10NumericText, False)

	@property
	def NetPmt(self):
		return self._NetPmt

	@NetPmt.setter
	def NetPmt(self, value):
		self._NetPmt = value if value is not None else base_types.UninitialisedField(self, 'NetPmt', AmountAndDirection86, False)

	@NetPmt.deleter
	def NetPmt(self):
		del self._NetPmt
		self._NetPmt = base_types.UninitialisedField(self, 'NetPmt', AmountAndDirection86, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssCdts', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssDbts', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatePmtConf', type=Max10NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetPmt', type=AmountAndDirection86, min=1, max=1, mutex_group=None, array=False),
	))