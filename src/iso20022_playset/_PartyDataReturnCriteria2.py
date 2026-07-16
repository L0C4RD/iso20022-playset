# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class PartyDataReturnCriteria2(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_ClsgDt", "_CtctDtls", "_LckSts", "_MktSpcfcAttr", "_Nm", "_OpngDt", "_PtyId", "_ResTp", "_RspnsblPtyId", "_RstrctdOnDt", "_RstrctnId", "_ShrtNm", "_TechAdr", "_Tp"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', RequestedIndicator, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', RequestedIndicator, False)

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', RequestedIndicator, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', RequestedIndicator, False)

	@property
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if value is not None else base_types.UninitialisedField(self, 'CtctDtls', RequestedIndicator, False)

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = base_types.UninitialisedField(self, 'CtctDtls', RequestedIndicator, False)

	@property
	def LckSts(self):
		return self._LckSts

	@LckSts.setter
	def LckSts(self, value):
		self._LckSts = value if value is not None else base_types.UninitialisedField(self, 'LckSts', RequestedIndicator, False)

	@LckSts.deleter
	def LckSts(self):
		del self._LckSts
		self._LckSts = base_types.UninitialisedField(self, 'LckSts', RequestedIndicator, False)

	@property
	def MktSpcfcAttr(self):
		return self._MktSpcfcAttr

	@MktSpcfcAttr.setter
	def MktSpcfcAttr(self, value):
		self._MktSpcfcAttr = value if value is not None else base_types.UninitialisedField(self, 'MktSpcfcAttr', RequestedIndicator, False)

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = base_types.UninitialisedField(self, 'MktSpcfcAttr', RequestedIndicator, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', RequestedIndicator, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', RequestedIndicator, False)

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if value is not None else base_types.UninitialisedField(self, 'OpngDt', RequestedIndicator, False)

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = base_types.UninitialisedField(self, 'OpngDt', RequestedIndicator, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', RequestedIndicator, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', RequestedIndicator, False)

	@property
	def ResTp(self):
		return self._ResTp

	@ResTp.setter
	def ResTp(self, value):
		self._ResTp = value if value is not None else base_types.UninitialisedField(self, 'ResTp', RequestedIndicator, False)

	@ResTp.deleter
	def ResTp(self):
		del self._ResTp
		self._ResTp = base_types.UninitialisedField(self, 'ResTp', RequestedIndicator, False)

	@property
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if value is not None else base_types.UninitialisedField(self, 'RspnsblPtyId', RequestedIndicator, False)

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = base_types.UninitialisedField(self, 'RspnsblPtyId', RequestedIndicator, False)

	@property
	def RstrctdOnDt(self):
		return self._RstrctdOnDt

	@RstrctdOnDt.setter
	def RstrctdOnDt(self, value):
		self._RstrctdOnDt = value if value is not None else base_types.UninitialisedField(self, 'RstrctdOnDt', RequestedIndicator, False)

	@RstrctdOnDt.deleter
	def RstrctdOnDt(self):
		del self._RstrctdOnDt
		self._RstrctdOnDt = base_types.UninitialisedField(self, 'RstrctdOnDt', RequestedIndicator, False)

	@property
	def RstrctnId(self):
		return self._RstrctnId

	@RstrctnId.setter
	def RstrctnId(self, value):
		self._RstrctnId = value if value is not None else base_types.UninitialisedField(self, 'RstrctnId', RequestedIndicator, False)

	@RstrctnId.deleter
	def RstrctnId(self):
		del self._RstrctnId
		self._RstrctnId = base_types.UninitialisedField(self, 'RstrctnId', RequestedIndicator, False)

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if value is not None else base_types.UninitialisedField(self, 'ShrtNm', RequestedIndicator, False)

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = base_types.UninitialisedField(self, 'ShrtNm', RequestedIndicator, False)

	@property
	def TechAdr(self):
		return self._TechAdr

	@TechAdr.setter
	def TechAdr(self, value):
		self._TechAdr = value if value is not None else base_types.UninitialisedField(self, 'TechAdr', RequestedIndicator, False)

	@TechAdr.deleter
	def TechAdr(self):
		del self._TechAdr
		self._TechAdr = base_types.UninitialisedField(self, 'TechAdr', RequestedIndicator, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', RequestedIndicator, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctDtls', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LckSts', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktSpcfcAttr', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ResTp', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPtyId', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctdOnDt', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnId', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechAdr', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))