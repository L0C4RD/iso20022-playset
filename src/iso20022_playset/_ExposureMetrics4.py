# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import AmountAndDirection53
from . import PrincipalAmount3

class ExposureMetrics4(base_types._BaseFieldType):

	__slots__ = ["_CollMktVal", "_CshCollAmt", "_LnVal", "_MktVal", "_MrgnLn", "_OutsdngMrgnLnAmt", "_PrncplAmt", "_ShrtMktValAmt"]
	@property
	def CollMktVal(self):
		return self._CollMktVal

	@CollMktVal.setter
	def CollMktVal(self, value):
		self._CollMktVal = value if value is not None else base_types.UninitialisedField(self, 'CollMktVal', AmountAndDirection53, False)

	@CollMktVal.deleter
	def CollMktVal(self):
		del self._CollMktVal
		self._CollMktVal = base_types.UninitialisedField(self, 'CollMktVal', AmountAndDirection53, False)

	@property
	def CshCollAmt(self):
		return self._CshCollAmt

	@CshCollAmt.setter
	def CshCollAmt(self, value):
		self._CshCollAmt = value if value is not None else base_types.UninitialisedField(self, 'CshCollAmt', AmountAndDirection53, False)

	@CshCollAmt.deleter
	def CshCollAmt(self):
		del self._CshCollAmt
		self._CshCollAmt = base_types.UninitialisedField(self, 'CshCollAmt', AmountAndDirection53, False)

	@property
	def LnVal(self):
		return self._LnVal

	@LnVal.setter
	def LnVal(self, value):
		self._LnVal = value if value is not None else base_types.UninitialisedField(self, 'LnVal', ActiveOrHistoricCurrencyAndAmount, False)

	@LnVal.deleter
	def LnVal(self):
		del self._LnVal
		self._LnVal = base_types.UninitialisedField(self, 'LnVal', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if value is not None else base_types.UninitialisedField(self, 'MktVal', AmountAndDirection53, False)

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = base_types.UninitialisedField(self, 'MktVal', AmountAndDirection53, False)

	@property
	def MrgnLn(self):
		return self._MrgnLn

	@MrgnLn.setter
	def MrgnLn(self, value):
		self._MrgnLn = value if value is not None else base_types.UninitialisedField(self, 'MrgnLn', ActiveOrHistoricCurrencyAndAmount, False)

	@MrgnLn.deleter
	def MrgnLn(self):
		del self._MrgnLn
		self._MrgnLn = base_types.UninitialisedField(self, 'MrgnLn', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def OutsdngMrgnLnAmt(self):
		return self._OutsdngMrgnLnAmt

	@OutsdngMrgnLnAmt.setter
	def OutsdngMrgnLnAmt(self, value):
		self._OutsdngMrgnLnAmt = value if value is not None else base_types.UninitialisedField(self, 'OutsdngMrgnLnAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@OutsdngMrgnLnAmt.deleter
	def OutsdngMrgnLnAmt(self):
		del self._OutsdngMrgnLnAmt
		self._OutsdngMrgnLnAmt = base_types.UninitialisedField(self, 'OutsdngMrgnLnAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def PrncplAmt(self):
		return self._PrncplAmt

	@PrncplAmt.setter
	def PrncplAmt(self, value):
		self._PrncplAmt = value if value is not None else base_types.UninitialisedField(self, 'PrncplAmt', PrincipalAmount3, False)

	@PrncplAmt.deleter
	def PrncplAmt(self):
		del self._PrncplAmt
		self._PrncplAmt = base_types.UninitialisedField(self, 'PrncplAmt', PrincipalAmount3, False)

	@property
	def ShrtMktValAmt(self):
		return self._ShrtMktValAmt

	@ShrtMktValAmt.setter
	def ShrtMktValAmt(self, value):
		self._ShrtMktValAmt = value if value is not None else base_types.UninitialisedField(self, 'ShrtMktValAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@ShrtMktValAmt.deleter
	def ShrtMktValAmt(self):
		del self._ShrtMktValAmt
		self._ShrtMktValAmt = base_types.UninitialisedField(self, 'ShrtMktValAmt', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollMktVal', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshCollAmt', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnLn', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngMrgnLnAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmt', type=PrincipalAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtMktValAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))