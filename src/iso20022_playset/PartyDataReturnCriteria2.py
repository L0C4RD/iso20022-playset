from . import base_types
from .RequestedIndicator import RequestedIndicator

class PartyDataReturnCriteria2(base_types._BaseFieldType):

	__slots__ = ["_ClsgDt", "_OpngDt", "_Adr", "_Tp", "_PtyId", "_LckSts", "_RspnsblPtyId", "_ResTp", "_TechAdr", "_Nm", "_MktSpcfcAttr", "_ShrtNm", "_RstrctdOnDt", "_RstrctnId", "_CtctDtls"]
	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != base_types.auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if type(value) != base_types.auto else self.make_default("OpngDt")

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def LckSts(self):
		return self._LckSts

	@LckSts.setter
	def LckSts(self, value):
		self._LckSts = value if type(value) != base_types.auto else self.make_default("LckSts")

	@LckSts.deleter
	def LckSts(self):
		del self._LckSts
		self._LckSts = None

	@property
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if type(value) != base_types.auto else self.make_default("RspnsblPtyId")

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = None

	@property
	def ResTp(self):
		return self._ResTp

	@ResTp.setter
	def ResTp(self, value):
		self._ResTp = value if type(value) != base_types.auto else self.make_default("ResTp")

	@ResTp.deleter
	def ResTp(self):
		del self._ResTp
		self._ResTp = None

	@property
	def TechAdr(self):
		return self._TechAdr

	@TechAdr.setter
	def TechAdr(self, value):
		self._TechAdr = value if type(value) != base_types.auto else self.make_default("TechAdr")

	@TechAdr.deleter
	def TechAdr(self):
		del self._TechAdr
		self._TechAdr = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def MktSpcfcAttr(self):
		return self._MktSpcfcAttr

	@MktSpcfcAttr.setter
	def MktSpcfcAttr(self, value):
		self._MktSpcfcAttr = value if type(value) != base_types.auto else self.make_default("MktSpcfcAttr")

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = None

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != base_types.auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

	@property
	def RstrctdOnDt(self):
		return self._RstrctdOnDt

	@RstrctdOnDt.setter
	def RstrctdOnDt(self, value):
		self._RstrctdOnDt = value if type(value) != base_types.auto else self.make_default("RstrctdOnDt")

	@RstrctdOnDt.deleter
	def RstrctdOnDt(self):
		del self._RstrctdOnDt
		self._RstrctdOnDt = None

	@property
	def RstrctnId(self):
		return self._RstrctnId

	@RstrctnId.setter
	def RstrctnId(self, value):
		self._RstrctnId = value if type(value) != base_types.auto else self.make_default("RstrctnId")

	@RstrctnId.deleter
	def RstrctnId(self):
		del self._RstrctnId
		self._RstrctnId = None

	@property
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if type(value) != base_types.auto else self.make_default("CtctDtls")

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgDt', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LckSts', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPtyId', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ResTp', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechAdr', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktSpcfcAttr', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctdOnDt', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnId', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctDtls', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

