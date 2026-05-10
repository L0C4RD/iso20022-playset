import base_types
import Pagination1
import Max100Text
import OrganisationIdentification15Choice
import ISODate
import Number

class TradeReportHeader4(base_types._BaseFieldType):

	__slots__ = ["_NbRcrds", "_CmptntAuthrty", "_MsgPgntn", "_NewTradRpstryIdr", "_RptExctnDt", "_RptgPurp"]
	@property
	def NbRcrds(self):
		return self._NbRcrds

	@NbRcrds.setter
	def NbRcrds(self, value):
		self._NbRcrds = value if type(value) != auto else self.make_default("NbRcrds")

	@NbRcrds.deleter
	def NbRcrds(self):
		del self._NbRcrds
		self._NbRcrds = None

	@property
	def CmptntAuthrty(self):
		return self._CmptntAuthrty

	@CmptntAuthrty.setter
	def CmptntAuthrty(self, value):
		self._CmptntAuthrty = value if type(value) != auto else self.make_default("CmptntAuthrty")

	@CmptntAuthrty.deleter
	def CmptntAuthrty(self):
		del self._CmptntAuthrty
		self._CmptntAuthrty = None

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if type(value) != auto else self.make_default("MsgPgntn")

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = None

	@property
	def NewTradRpstryIdr(self):
		return self._NewTradRpstryIdr

	@NewTradRpstryIdr.setter
	def NewTradRpstryIdr(self, value):
		self._NewTradRpstryIdr = value if type(value) != auto else self.make_default("NewTradRpstryIdr")

	@NewTradRpstryIdr.deleter
	def NewTradRpstryIdr(self):
		del self._NewTradRpstryIdr
		self._NewTradRpstryIdr = None

	@property
	def RptExctnDt(self):
		return self._RptExctnDt

	@RptExctnDt.setter
	def RptExctnDt(self, value):
		self._RptExctnDt = value if type(value) != auto else self.make_default("RptExctnDt")

	@RptExctnDt.deleter
	def RptExctnDt(self):
		del self._RptExctnDt
		self._RptExctnDt = None

	@property
	def RptgPurp(self):
		return self._RptgPurp

	@RptgPurp.setter
	def RptgPurp(self, value):
		self._RptgPurp = value if type(value) != auto else self.make_default("RptgPurp")

	@RptgPurp.deleter
	def RptgPurp(self):
		del self._RptgPurp
		self._RptgPurp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbRcrds', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmptntAuthrty', type=Max100Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewTradRpstryIdr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptExctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPurp', type=Max100Text, min=0, max=None, mutex_group=None, array=True),
	))

