from . import base_types
import DateAndDateTime2Choice
import CreditDebitCode
import System3
import PaymentStatus6
import PaymentOrigin1Choice

class PaymentCommon6(base_types._BaseFieldType):

	__slots__ = ["_PmtMtd", "_ReqdExctnDt", "_NtryDt", "_CdtDbtInd", "_PmtFr", "_PmtTo", "_CmonSts"]
	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if type(value) != auto else self.make_default("PmtMtd")

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = None

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if type(value) != auto else self.make_default("ReqdExctnDt")

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = None

	@property
	def NtryDt(self):
		return self._NtryDt

	@NtryDt.setter
	def NtryDt(self, value):
		self._NtryDt = value if type(value) != auto else self.make_default("NtryDt")

	@NtryDt.deleter
	def NtryDt(self):
		del self._NtryDt
		self._NtryDt = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def PmtFr(self):
		return self._PmtFr

	@PmtFr.setter
	def PmtFr(self, value):
		self._PmtFr = value if type(value) != auto else self.make_default("PmtFr")

	@PmtFr.deleter
	def PmtFr(self):
		del self._PmtFr
		self._PmtFr = None

	@property
	def PmtTo(self):
		return self._PmtTo

	@PmtTo.setter
	def PmtTo(self, value):
		self._PmtTo = value if type(value) != auto else self.make_default("PmtTo")

	@PmtTo.deleter
	def PmtTo(self):
		del self._PmtTo
		self._PmtTo = None

	@property
	def CmonSts(self):
		return self._CmonSts

	@CmonSts.setter
	def CmonSts(self, value):
		self._CmonSts = value if type(value) != auto else self.make_default("CmonSts")

	@CmonSts.deleter
	def CmonSts(self):
		del self._CmonSts
		self._CmonSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtMtd', type=PaymentOrigin1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFr', type=System3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTo', type=System3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonSts', type=PaymentStatus6, min=0, max=None, mutex_group=None, array=True),
	))

