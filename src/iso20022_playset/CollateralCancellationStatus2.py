import base_types
import Max35Text
import RejectionStatus3
import Status4Code

class CollateralCancellationStatus2(base_types._BaseFieldType):

	__slots__ = ["_CollStsCd", "_RjctnDtls", "_AddtlInf"]
	@property
	def CollStsCd(self):
		return self._CollStsCd

	@CollStsCd.setter
	def CollStsCd(self, value):
		self._CollStsCd = value if type(value) != auto else self.make_default("CollStsCd")

	@CollStsCd.deleter
	def CollStsCd(self):
		del self._CollStsCd
		self._CollStsCd = None

	@property
	def RjctnDtls(self):
		return self._RjctnDtls

	@RjctnDtls.setter
	def RjctnDtls(self, value):
		self._RjctnDtls = value if type(value) != auto else self.make_default("RjctnDtls")

	@RjctnDtls.deleter
	def RjctnDtls(self):
		del self._RjctnDtls
		self._RjctnDtls = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollStsCd', type=Status4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnDtls', type=RejectionStatus3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

