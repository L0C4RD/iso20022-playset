import base_types
import CardType1Code
import ISOYearMonth
import Max3Text
import PartyIdentification125Choice
import Max35Text

class PaymentCard29(base_types._BaseFieldType):

	__slots__ = ["_HldrNm", "_XpryDt", "_Nb", "_Tp", "_StartDt", "_CardIssrId", "_SctyCd", "_CardIssrNm", "_SeqNb"]
	@property
	def HldrNm(self):
		return self._HldrNm

	@HldrNm.setter
	def HldrNm(self, value):
		self._HldrNm = value if type(value) != auto else self.make_default("HldrNm")

	@HldrNm.deleter
	def HldrNm(self):
		del self._HldrNm
		self._HldrNm = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

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

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	@property
	def CardIssrId(self):
		return self._CardIssrId

	@CardIssrId.setter
	def CardIssrId(self, value):
		self._CardIssrId = value if type(value) != auto else self.make_default("CardIssrId")

	@CardIssrId.deleter
	def CardIssrId(self):
		del self._CardIssrId
		self._CardIssrId = None

	@property
	def SctyCd(self):
		return self._SctyCd

	@SctyCd.setter
	def SctyCd(self, value):
		self._SctyCd = value if type(value) != auto else self.make_default("SctyCd")

	@SctyCd.deleter
	def SctyCd(self):
		del self._SctyCd
		self._SctyCd = None

	@property
	def CardIssrNm(self):
		return self._CardIssrNm

	@CardIssrNm.setter
	def CardIssrNm(self, value):
		self._CardIssrNm = value if type(value) != auto else self.make_default("CardIssrNm")

	@CardIssrNm.deleter
	def CardIssrNm(self):
		del self._CardIssrNm
		self._CardIssrNm = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HldrNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISOYearMonth, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CardType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardIssrId', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardIssrNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
	))

