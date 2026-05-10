import base_types
import PartyIdentification135
import ActiveOrHistoricCurrencyAndAmount
import ISODate
import GarnishmentType1
import TrueFalseIndicator
import Max140Text

class Garnishment3(base_types._BaseFieldType):

	__slots__ = ["_MplyeeTermntnInd", "_Dt", "_FmlyMdclInsrncInd", "_Grnshee", "_RmtdAmt", "_GrnshmtAdmstr", "_RefNb", "_Tp"]
	@property
	def MplyeeTermntnInd(self):
		return self._MplyeeTermntnInd

	@MplyeeTermntnInd.setter
	def MplyeeTermntnInd(self, value):
		self._MplyeeTermntnInd = value if type(value) != auto else self.make_default("MplyeeTermntnInd")

	@MplyeeTermntnInd.deleter
	def MplyeeTermntnInd(self):
		del self._MplyeeTermntnInd
		self._MplyeeTermntnInd = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def FmlyMdclInsrncInd(self):
		return self._FmlyMdclInsrncInd

	@FmlyMdclInsrncInd.setter
	def FmlyMdclInsrncInd(self, value):
		self._FmlyMdclInsrncInd = value if type(value) != auto else self.make_default("FmlyMdclInsrncInd")

	@FmlyMdclInsrncInd.deleter
	def FmlyMdclInsrncInd(self):
		del self._FmlyMdclInsrncInd
		self._FmlyMdclInsrncInd = None

	@property
	def Grnshee(self):
		return self._Grnshee

	@Grnshee.setter
	def Grnshee(self, value):
		self._Grnshee = value if type(value) != auto else self.make_default("Grnshee")

	@Grnshee.deleter
	def Grnshee(self):
		del self._Grnshee
		self._Grnshee = None

	@property
	def RmtdAmt(self):
		return self._RmtdAmt

	@RmtdAmt.setter
	def RmtdAmt(self, value):
		self._RmtdAmt = value if type(value) != auto else self.make_default("RmtdAmt")

	@RmtdAmt.deleter
	def RmtdAmt(self):
		del self._RmtdAmt
		self._RmtdAmt = None

	@property
	def GrnshmtAdmstr(self):
		return self._GrnshmtAdmstr

	@GrnshmtAdmstr.setter
	def GrnshmtAdmstr(self, value):
		self._GrnshmtAdmstr = value if type(value) != auto else self.make_default("GrnshmtAdmstr")

	@GrnshmtAdmstr.deleter
	def GrnshmtAdmstr(self):
		del self._GrnshmtAdmstr
		self._GrnshmtAdmstr = None

	@property
	def RefNb(self):
		return self._RefNb

	@RefNb.setter
	def RefNb(self, value):
		self._RefNb = value if type(value) != auto else self.make_default("RefNb")

	@RefNb.deleter
	def RefNb(self):
		del self._RefNb
		self._RefNb = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MplyeeTermntnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FmlyMdclInsrncInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grnshee', type=PartyIdentification135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrnshmtAdmstr', type=PartyIdentification135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefNb', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=GarnishmentType1, min=1, max=1, mutex_group=None, array=False),
	))

