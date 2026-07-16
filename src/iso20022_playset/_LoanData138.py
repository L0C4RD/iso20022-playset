# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import CollateralDeliveryMethod1Code
from . import ISODate
from . import ISODateTime
from . import InterestRate6
from . import MICIdentifier
from . import Max52Text

class LoanData138(base_types._BaseFieldType):

	__slots__ = ["_CollDlvryMtd", "_EvtDt", "_ExctnDtTm", "_MrgnLnAttr", "_OutsdngMrgnLnAmt", "_ShrtMktValAmt", "_TermntnDt", "_TradgVn", "_UnqTradIdr"]
	@property
	def CollDlvryMtd(self):
		return self._CollDlvryMtd

	@CollDlvryMtd.setter
	def CollDlvryMtd(self, value):
		self._CollDlvryMtd = value if value is not None else base_types.UninitialisedField(self, 'CollDlvryMtd', CollateralDeliveryMethod1Code, False)

	@CollDlvryMtd.deleter
	def CollDlvryMtd(self):
		del self._CollDlvryMtd
		self._CollDlvryMtd = base_types.UninitialisedField(self, 'CollDlvryMtd', CollateralDeliveryMethod1Code, False)

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if value is not None else base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if value is not None else base_types.UninitialisedField(self, 'ExctnDtTm', ISODateTime, False)

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = base_types.UninitialisedField(self, 'ExctnDtTm', ISODateTime, False)

	@property
	def MrgnLnAttr(self):
		return self._MrgnLnAttr

	@MrgnLnAttr.setter
	def MrgnLnAttr(self, value):
		self._MrgnLnAttr = value if value is not None else base_types.UninitialisedField(self, 'MrgnLnAttr', InterestRate6, True)

	@MrgnLnAttr.deleter
	def MrgnLnAttr(self):
		del self._MrgnLnAttr
		self._MrgnLnAttr = base_types.UninitialisedField(self, 'MrgnLnAttr', InterestRate6, True)

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
	def ShrtMktValAmt(self):
		return self._ShrtMktValAmt

	@ShrtMktValAmt.setter
	def ShrtMktValAmt(self, value):
		self._ShrtMktValAmt = value if value is not None else base_types.UninitialisedField(self, 'ShrtMktValAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@ShrtMktValAmt.deleter
	def ShrtMktValAmt(self):
		del self._ShrtMktValAmt
		self._ShrtMktValAmt = base_types.UninitialisedField(self, 'ShrtMktValAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if value is not None else base_types.UninitialisedField(self, 'TermntnDt', ISODate, False)

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = base_types.UninitialisedField(self, 'TermntnDt', ISODate, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTradIdr', Max52Text, False)

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = base_types.UninitialisedField(self, 'UnqTradIdr', Max52Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollDlvryMtd', type=CollateralDeliveryMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnLnAttr', type=InterestRate6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OutsdngMrgnLnAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtMktValAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTradIdr', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
	))