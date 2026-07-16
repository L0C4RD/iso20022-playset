# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import LanguageCode
from . import Max2000Text
from . import Max35Text
from . import xs:IDREF

class EventDescription1(base_types._BaseFieldType):

	__slots__ = ["_Advsr", "_AssoctdDoc", "_Desc", "_Dt", "_GovngCtrct", "_Idr", "_LangCd", "_LglCntxt", "_OthrPty", "_Rcpt", "_RltdDoc", "_RltdLttr", "_RltdMsg"]
	@property
	def Advsr(self):
		return self._Advsr

	@Advsr.setter
	def Advsr(self, value):
		self._Advsr = value if value is not None else base_types.UninitialisedField(self, 'Advsr', xs:IDREF, False)

	@Advsr.deleter
	def Advsr(self):
		del self._Advsr
		self._Advsr = base_types.UninitialisedField(self, 'Advsr', xs:IDREF, False)

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if value is not None else base_types.UninitialisedField(self, 'AssoctdDoc', xs:IDREF, True)

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = base_types.UninitialisedField(self, 'AssoctdDoc', xs:IDREF, True)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max2000Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max2000Text, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODateTime, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODateTime, False)

	@property
	def GovngCtrct(self):
		return self._GovngCtrct

	@GovngCtrct.setter
	def GovngCtrct(self, value):
		self._GovngCtrct = value if value is not None else base_types.UninitialisedField(self, 'GovngCtrct', xs:IDREF, True)

	@GovngCtrct.deleter
	def GovngCtrct(self):
		del self._GovngCtrct
		self._GovngCtrct = base_types.UninitialisedField(self, 'GovngCtrct', xs:IDREF, True)

	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if value is not None else base_types.UninitialisedField(self, 'Idr', Max35Text, False)

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = base_types.UninitialisedField(self, 'Idr', Max35Text, False)

	@property
	def LangCd(self):
		return self._LangCd

	@LangCd.setter
	def LangCd(self, value):
		self._LangCd = value if value is not None else base_types.UninitialisedField(self, 'LangCd', LanguageCode, False)

	@LangCd.deleter
	def LangCd(self):
		del self._LangCd
		self._LangCd = base_types.UninitialisedField(self, 'LangCd', LanguageCode, False)

	@property
	def LglCntxt(self):
		return self._LglCntxt

	@LglCntxt.setter
	def LglCntxt(self, value):
		self._LglCntxt = value if value is not None else base_types.UninitialisedField(self, 'LglCntxt', xs:IDREF, False)

	@LglCntxt.deleter
	def LglCntxt(self):
		del self._LglCntxt
		self._LglCntxt = base_types.UninitialisedField(self, 'LglCntxt', xs:IDREF, False)

	@property
	def OthrPty(self):
		return self._OthrPty

	@OthrPty.setter
	def OthrPty(self, value):
		self._OthrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrPty', xs:IDREF, True)

	@OthrPty.deleter
	def OthrPty(self):
		del self._OthrPty
		self._OthrPty = base_types.UninitialisedField(self, 'OthrPty', xs:IDREF, True)

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if value is not None else base_types.UninitialisedField(self, 'Rcpt', xs:IDREF, False)

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = base_types.UninitialisedField(self, 'Rcpt', xs:IDREF, False)

	@property
	def RltdDoc(self):
		return self._RltdDoc

	@RltdDoc.setter
	def RltdDoc(self, value):
		self._RltdDoc = value if value is not None else base_types.UninitialisedField(self, 'RltdDoc', xs:IDREF, True)

	@RltdDoc.deleter
	def RltdDoc(self):
		del self._RltdDoc
		self._RltdDoc = base_types.UninitialisedField(self, 'RltdDoc', xs:IDREF, True)

	@property
	def RltdLttr(self):
		return self._RltdLttr

	@RltdLttr.setter
	def RltdLttr(self, value):
		self._RltdLttr = value if value is not None else base_types.UninitialisedField(self, 'RltdLttr', xs:IDREF, True)

	@RltdLttr.deleter
	def RltdLttr(self):
		del self._RltdLttr
		self._RltdLttr = base_types.UninitialisedField(self, 'RltdLttr', xs:IDREF, True)

	@property
	def RltdMsg(self):
		return self._RltdMsg

	@RltdMsg.setter
	def RltdMsg(self, value):
		self._RltdMsg = value if value is not None else base_types.UninitialisedField(self, 'RltdMsg', xs:IDREF, True)

	@RltdMsg.deleter
	def RltdMsg(self):
		del self._RltdMsg
		self._RltdMsg = base_types.UninitialisedField(self, 'RltdMsg', xs:IDREF, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Advsr', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovngCtrct', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Idr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LangCd', type=LanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglCntxt', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPty', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcpt', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdLttr', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdMsg', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
	))