import base_types
import ActiveOrHistoricCurrencyAndAmount
import PrincipalAmount3
import AmountAndDirection53

class ExposureMetrics4(base_types._BaseFieldType):

	__slots__ = ["_LnVal", "_MrgnLn", "_ShrtMktValAmt", "_OutsdngMrgnLnAmt", "_CollMktVal", "_CshCollAmt", "_PrncplAmt", "_MktVal"]
	@property
	def LnVal(self):
		return self._LnVal

	@LnVal.setter
	def LnVal(self, value):
		self._LnVal = value if type(value) != auto else self.make_default("LnVal")

	@LnVal.deleter
	def LnVal(self):
		del self._LnVal
		self._LnVal = None

	@property
	def MrgnLn(self):
		return self._MrgnLn

	@MrgnLn.setter
	def MrgnLn(self, value):
		self._MrgnLn = value if type(value) != auto else self.make_default("MrgnLn")

	@MrgnLn.deleter
	def MrgnLn(self):
		del self._MrgnLn
		self._MrgnLn = None

	@property
	def ShrtMktValAmt(self):
		return self._ShrtMktValAmt

	@ShrtMktValAmt.setter
	def ShrtMktValAmt(self, value):
		self._ShrtMktValAmt = value if type(value) != auto else self.make_default("ShrtMktValAmt")

	@ShrtMktValAmt.deleter
	def ShrtMktValAmt(self):
		del self._ShrtMktValAmt
		self._ShrtMktValAmt = None

	@property
	def OutsdngMrgnLnAmt(self):
		return self._OutsdngMrgnLnAmt

	@OutsdngMrgnLnAmt.setter
	def OutsdngMrgnLnAmt(self, value):
		self._OutsdngMrgnLnAmt = value if type(value) != auto else self.make_default("OutsdngMrgnLnAmt")

	@OutsdngMrgnLnAmt.deleter
	def OutsdngMrgnLnAmt(self):
		del self._OutsdngMrgnLnAmt
		self._OutsdngMrgnLnAmt = None

	@property
	def CollMktVal(self):
		return self._CollMktVal

	@CollMktVal.setter
	def CollMktVal(self, value):
		self._CollMktVal = value if type(value) != auto else self.make_default("CollMktVal")

	@CollMktVal.deleter
	def CollMktVal(self):
		del self._CollMktVal
		self._CollMktVal = None

	@property
	def CshCollAmt(self):
		return self._CshCollAmt

	@CshCollAmt.setter
	def CshCollAmt(self, value):
		self._CshCollAmt = value if type(value) != auto else self.make_default("CshCollAmt")

	@CshCollAmt.deleter
	def CshCollAmt(self):
		del self._CshCollAmt
		self._CshCollAmt = None

	@property
	def PrncplAmt(self):
		return self._PrncplAmt

	@PrncplAmt.setter
	def PrncplAmt(self, value):
		self._PrncplAmt = value if type(value) != auto else self.make_default("PrncplAmt")

	@PrncplAmt.deleter
	def PrncplAmt(self):
		del self._PrncplAmt
		self._PrncplAmt = None

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LnVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnLn', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtMktValAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngMrgnLnAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMktVal', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshCollAmt', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmt', type=PrincipalAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
	))

