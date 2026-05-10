from . import base_types
from .YesNoIndicator import YesNoIndicator
from .Max70Text import Max70Text
from .BICIdentification1 import BICIdentification1
from .TradeCertificateType1Code import TradeCertificateType1Code
from .PartyIdentification27 import PartyIdentification27

class RequiredSubmission4(base_types._BaseFieldType):

	__slots__ = ["_MtchConsgn", "_CertTp", "_AuthrsdInspctrInd", "_Submitr", "_LineItmId", "_MtchManfctr", "_MtchIssr", "_MtchInspctnDt", "_MtchIsseDt"]
	@property
	def MtchConsgn(self):
		return self._MtchConsgn

	@MtchConsgn.setter
	def MtchConsgn(self, value):
		self._MtchConsgn = value if type(value) != auto else self.make_default("MtchConsgn")

	@MtchConsgn.deleter
	def MtchConsgn(self):
		del self._MtchConsgn
		self._MtchConsgn = None

	@property
	def CertTp(self):
		return self._CertTp

	@CertTp.setter
	def CertTp(self, value):
		self._CertTp = value if type(value) != auto else self.make_default("CertTp")

	@CertTp.deleter
	def CertTp(self):
		del self._CertTp
		self._CertTp = None

	@property
	def AuthrsdInspctrInd(self):
		return self._AuthrsdInspctrInd

	@AuthrsdInspctrInd.setter
	def AuthrsdInspctrInd(self, value):
		self._AuthrsdInspctrInd = value if type(value) != auto else self.make_default("AuthrsdInspctrInd")

	@AuthrsdInspctrInd.deleter
	def AuthrsdInspctrInd(self):
		del self._AuthrsdInspctrInd
		self._AuthrsdInspctrInd = None

	@property
	def Submitr(self):
		return self._Submitr

	@Submitr.setter
	def Submitr(self, value):
		self._Submitr = value if type(value) != auto else self.make_default("Submitr")

	@Submitr.deleter
	def Submitr(self):
		del self._Submitr
		self._Submitr = None

	@property
	def LineItmId(self):
		return self._LineItmId

	@LineItmId.setter
	def LineItmId(self, value):
		self._LineItmId = value if type(value) != auto else self.make_default("LineItmId")

	@LineItmId.deleter
	def LineItmId(self):
		del self._LineItmId
		self._LineItmId = None

	@property
	def MtchManfctr(self):
		return self._MtchManfctr

	@MtchManfctr.setter
	def MtchManfctr(self, value):
		self._MtchManfctr = value if type(value) != auto else self.make_default("MtchManfctr")

	@MtchManfctr.deleter
	def MtchManfctr(self):
		del self._MtchManfctr
		self._MtchManfctr = None

	@property
	def MtchIssr(self):
		return self._MtchIssr

	@MtchIssr.setter
	def MtchIssr(self, value):
		self._MtchIssr = value if type(value) != auto else self.make_default("MtchIssr")

	@MtchIssr.deleter
	def MtchIssr(self):
		del self._MtchIssr
		self._MtchIssr = None

	@property
	def MtchInspctnDt(self):
		return self._MtchInspctnDt

	@MtchInspctnDt.setter
	def MtchInspctnDt(self, value):
		self._MtchInspctnDt = value if type(value) != auto else self.make_default("MtchInspctnDt")

	@MtchInspctnDt.deleter
	def MtchInspctnDt(self):
		del self._MtchInspctnDt
		self._MtchInspctnDt = None

	@property
	def MtchIsseDt(self):
		return self._MtchIsseDt

	@MtchIsseDt.setter
	def MtchIsseDt(self, value):
		self._MtchIsseDt = value if type(value) != auto else self.make_default("MtchIsseDt")

	@MtchIsseDt.deleter
	def MtchIsseDt(self):
		del self._MtchIsseDt
		self._MtchIsseDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtchConsgn', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertTp', type=TradeCertificateType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdInspctrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LineItmId', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtchManfctr', type=PartyIdentification27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchIssr', type=PartyIdentification27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchInspctnDt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchIsseDt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

