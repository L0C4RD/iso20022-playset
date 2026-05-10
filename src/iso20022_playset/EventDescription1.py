import base_types
import ISODateTime
import Max35Text
import LanguageCode
import Max2000Text
import xs:IDREF

class EventDescription1(base_types._BaseFieldType):

	__slots__ = ["_LglCntxt", "_OthrPty", "_RltdDoc", "_RltdLttr", "_LangCd", "_GovngCtrct", "_RltdMsg", "_Dt", "_Advsr", "_Rcpt", "_Idr", "_Desc", "_AssoctdDoc"]
	@property
	def LglCntxt(self):
		return self._LglCntxt

	@LglCntxt.setter
	def LglCntxt(self, value):
		self._LglCntxt = value if type(value) != auto else self.make_default("LglCntxt")

	@LglCntxt.deleter
	def LglCntxt(self):
		del self._LglCntxt
		self._LglCntxt = None

	@property
	def OthrPty(self):
		return self._OthrPty

	@OthrPty.setter
	def OthrPty(self, value):
		self._OthrPty = value if type(value) != auto else self.make_default("OthrPty")

	@OthrPty.deleter
	def OthrPty(self):
		del self._OthrPty
		self._OthrPty = None

	@property
	def RltdDoc(self):
		return self._RltdDoc

	@RltdDoc.setter
	def RltdDoc(self, value):
		self._RltdDoc = value if type(value) != auto else self.make_default("RltdDoc")

	@RltdDoc.deleter
	def RltdDoc(self):
		del self._RltdDoc
		self._RltdDoc = None

	@property
	def RltdLttr(self):
		return self._RltdLttr

	@RltdLttr.setter
	def RltdLttr(self, value):
		self._RltdLttr = value if type(value) != auto else self.make_default("RltdLttr")

	@RltdLttr.deleter
	def RltdLttr(self):
		del self._RltdLttr
		self._RltdLttr = None

	@property
	def LangCd(self):
		return self._LangCd

	@LangCd.setter
	def LangCd(self, value):
		self._LangCd = value if type(value) != auto else self.make_default("LangCd")

	@LangCd.deleter
	def LangCd(self):
		del self._LangCd
		self._LangCd = None

	@property
	def GovngCtrct(self):
		return self._GovngCtrct

	@GovngCtrct.setter
	def GovngCtrct(self, value):
		self._GovngCtrct = value if type(value) != auto else self.make_default("GovngCtrct")

	@GovngCtrct.deleter
	def GovngCtrct(self):
		del self._GovngCtrct
		self._GovngCtrct = None

	@property
	def RltdMsg(self):
		return self._RltdMsg

	@RltdMsg.setter
	def RltdMsg(self, value):
		self._RltdMsg = value if type(value) != auto else self.make_default("RltdMsg")

	@RltdMsg.deleter
	def RltdMsg(self):
		del self._RltdMsg
		self._RltdMsg = None

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
	def Advsr(self):
		return self._Advsr

	@Advsr.setter
	def Advsr(self, value):
		self._Advsr = value if type(value) != auto else self.make_default("Advsr")

	@Advsr.deleter
	def Advsr(self):
		del self._Advsr
		self._Advsr = None

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if type(value) != auto else self.make_default("Rcpt")

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = None

	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if type(value) != auto else self.make_default("Idr")

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if type(value) != auto else self.make_default("AssoctdDoc")

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LglCntxt', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPty', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdLttr', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LangCd', type=LanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovngCtrct', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdMsg', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Advsr', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
	))

