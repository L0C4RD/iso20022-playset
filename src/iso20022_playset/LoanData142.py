from . import base_types
import ISODate
import InterestRate6
import MICIdentifier
import Max52Text
import ISODateTime
import CollateralDeliveryMethod1Code
import ActiveOrHistoricCurrencyAndAmount

class LoanData142(base_types._BaseFieldType):

	__slots__ = ["_TermntnDt", "_MrgnLnAttr", "_ExctnDtTm", "_TradgVn", "_UnqTradIdr", "_OutsdngMrgnLnAmt", "_CollDlvryMtd", "_EvtDt", "_ShrtMktValAmt"]
	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

	@property
	def MrgnLnAttr(self):
		return self._MrgnLnAttr

	@MrgnLnAttr.setter
	def MrgnLnAttr(self, value):
		self._MrgnLnAttr = value if type(value) != auto else self.make_default("MrgnLnAttr")

	@MrgnLnAttr.deleter
	def MrgnLnAttr(self):
		del self._MrgnLnAttr
		self._MrgnLnAttr = None

	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if type(value) != auto else self.make_default("ExctnDtTm")

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if type(value) != auto else self.make_default("UnqTradIdr")

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = None

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
	def CollDlvryMtd(self):
		return self._CollDlvryMtd

	@CollDlvryMtd.setter
	def CollDlvryMtd(self, value):
		self._CollDlvryMtd = value if type(value) != auto else self.make_default("CollDlvryMtd")

	@CollDlvryMtd.deleter
	def CollDlvryMtd(self):
		del self._CollDlvryMtd
		self._CollDlvryMtd = None

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if type(value) != auto else self.make_default("EvtDt")

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='TermntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnLnAttr', type=InterestRate6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ExctnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTradIdr', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngMrgnLnAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollDlvryMtd', type=CollateralDeliveryMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtMktValAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

