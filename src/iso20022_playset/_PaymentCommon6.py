# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebitCode
from . import DateAndDateTime2Choice
from . import PaymentOrigin1Choice
from . import PaymentStatus6
from . import System3

class PaymentCommon6(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_CmonSts", "_NtryDt", "_PmtFr", "_PmtMtd", "_PmtTo", "_ReqdExctnDt"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def CmonSts(self):
		return self._CmonSts

	@CmonSts.setter
	def CmonSts(self, value):
		self._CmonSts = value if value is not None else base_types.UninitialisedField(self, 'CmonSts', PaymentStatus6, True)

	@CmonSts.deleter
	def CmonSts(self):
		del self._CmonSts
		self._CmonSts = base_types.UninitialisedField(self, 'CmonSts', PaymentStatus6, True)

	@property
	def NtryDt(self):
		return self._NtryDt

	@NtryDt.setter
	def NtryDt(self, value):
		self._NtryDt = value if value is not None else base_types.UninitialisedField(self, 'NtryDt', DateAndDateTime2Choice, False)

	@NtryDt.deleter
	def NtryDt(self):
		del self._NtryDt
		self._NtryDt = base_types.UninitialisedField(self, 'NtryDt', DateAndDateTime2Choice, False)

	@property
	def PmtFr(self):
		return self._PmtFr

	@PmtFr.setter
	def PmtFr(self, value):
		self._PmtFr = value if value is not None else base_types.UninitialisedField(self, 'PmtFr', System3, False)

	@PmtFr.deleter
	def PmtFr(self):
		del self._PmtFr
		self._PmtFr = base_types.UninitialisedField(self, 'PmtFr', System3, False)

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if value is not None else base_types.UninitialisedField(self, 'PmtMtd', PaymentOrigin1Choice, False)

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = base_types.UninitialisedField(self, 'PmtMtd', PaymentOrigin1Choice, False)

	@property
	def PmtTo(self):
		return self._PmtTo

	@PmtTo.setter
	def PmtTo(self, value):
		self._PmtTo = value if value is not None else base_types.UninitialisedField(self, 'PmtTo', System3, False)

	@PmtTo.deleter
	def PmtTo(self):
		del self._PmtTo
		self._PmtTo = base_types.UninitialisedField(self, 'PmtTo', System3, False)

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDt', DateAndDateTime2Choice, False)

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = base_types.UninitialisedField(self, 'ReqdExctnDt', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonSts', type=PaymentStatus6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtryDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFr', type=System3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=PaymentOrigin1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTo', type=System3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))