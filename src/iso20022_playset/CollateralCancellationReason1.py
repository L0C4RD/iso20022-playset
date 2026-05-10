import base_types
import CollateralCancellationType1Choice
import Max35Text

class CollateralCancellationReason1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CxlRsnCd"]
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

	@property
	def CxlRsnCd(self):
		return self._CxlRsnCd

	@CxlRsnCd.setter
	def CxlRsnCd(self, value):
		self._CxlRsnCd = value if type(value) != auto else self.make_default("CxlRsnCd")

	@CxlRsnCd.deleter
	def CxlRsnCd(self):
		del self._CxlRsnCd
		self._CxlRsnCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsnCd', type=CollateralCancellationType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

