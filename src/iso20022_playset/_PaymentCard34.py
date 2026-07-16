# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardType1Code
from . import ISOYearMonth
from . import Max35Text
from . import Max3Text
from . import PartyIdentification139

class PaymentCard34(base_types._BaseFieldType):

	__slots__ = ["_CardIssrId", "_CardIssrNm", "_HldrNm", "_Nb", "_SctyCd", "_SeqNb", "_StartDt", "_Tp", "_XpryDt"]
	@property
	def CardIssrId(self):
		return self._CardIssrId

	@CardIssrId.setter
	def CardIssrId(self, value):
		self._CardIssrId = value if value is not None else base_types.UninitialisedField(self, 'CardIssrId', PartyIdentification139, False)

	@CardIssrId.deleter
	def CardIssrId(self):
		del self._CardIssrId
		self._CardIssrId = base_types.UninitialisedField(self, 'CardIssrId', PartyIdentification139, False)

	@property
	def CardIssrNm(self):
		return self._CardIssrNm

	@CardIssrNm.setter
	def CardIssrNm(self, value):
		self._CardIssrNm = value if value is not None else base_types.UninitialisedField(self, 'CardIssrNm', Max35Text, False)

	@CardIssrNm.deleter
	def CardIssrNm(self):
		del self._CardIssrNm
		self._CardIssrNm = base_types.UninitialisedField(self, 'CardIssrNm', Max35Text, False)

	@property
	def HldrNm(self):
		return self._HldrNm

	@HldrNm.setter
	def HldrNm(self, value):
		self._HldrNm = value if value is not None else base_types.UninitialisedField(self, 'HldrNm', Max35Text, False)

	@HldrNm.deleter
	def HldrNm(self):
		del self._HldrNm
		self._HldrNm = base_types.UninitialisedField(self, 'HldrNm', Max35Text, False)

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@property
	def SctyCd(self):
		return self._SctyCd

	@SctyCd.setter
	def SctyCd(self, value):
		self._SctyCd = value if value is not None else base_types.UninitialisedField(self, 'SctyCd', Max35Text, False)

	@SctyCd.deleter
	def SctyCd(self):
		del self._SctyCd
		self._SctyCd = base_types.UninitialisedField(self, 'SctyCd', Max35Text, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Max3Text, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Max3Text, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISOYearMonth, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISOYearMonth, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CardType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CardType1Code, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', ISOYearMonth, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', ISOYearMonth, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardIssrId', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardIssrNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldrNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CardType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISOYearMonth, min=1, max=1, mutex_group=None, array=False),
	))