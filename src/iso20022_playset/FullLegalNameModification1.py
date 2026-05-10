import base_types
import Modification1Code
import Max350Text

class FullLegalNameModification1(base_types._BaseFieldType):

	__slots__ = ["_ModCd", "_FullLglNm"]
	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if type(value) != auto else self.make_default("ModCd")

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = None

	@property
	def FullLglNm(self):
		return self._FullLglNm

	@FullLglNm.setter
	def FullLglNm(self, value):
		self._FullLglNm = value if type(value) != auto else self.make_default("FullLglNm")

	@FullLglNm.deleter
	def FullLglNm(self):
		del self._FullLglNm
		self._FullLglNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullLglNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))

