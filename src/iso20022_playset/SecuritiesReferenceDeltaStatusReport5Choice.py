import base_types
import SecuritiesReferenceDataReport6
import SecuritiesReferenceDataReport7

class SecuritiesReferenceDeltaStatusReport5Choice(base_types._BaseFieldType):

	__slots__ = ["_CancRcrd", "_TermntdRcrd", "_ModfdRcrd", "_NewRcrd"]
	@property
	def CancRcrd(self):
		return self._CancRcrd

	@CancRcrd.setter
	def CancRcrd(self, value):
		self._CancRcrd = value if type(value) != auto else self.make_default("CancRcrd")

	@CancRcrd.deleter
	def CancRcrd(self):
		del self._CancRcrd
		self._CancRcrd = None

	@property
	def TermntdRcrd(self):
		return self._TermntdRcrd

	@TermntdRcrd.setter
	def TermntdRcrd(self, value):
		self._TermntdRcrd = value if type(value) != auto else self.make_default("TermntdRcrd")

	@TermntdRcrd.deleter
	def TermntdRcrd(self):
		del self._TermntdRcrd
		self._TermntdRcrd = None

	@property
	def ModfdRcrd(self):
		return self._ModfdRcrd

	@ModfdRcrd.setter
	def ModfdRcrd(self, value):
		self._ModfdRcrd = value if type(value) != auto else self.make_default("ModfdRcrd")

	@ModfdRcrd.deleter
	def ModfdRcrd(self):
		del self._ModfdRcrd
		self._ModfdRcrd = None

	@property
	def NewRcrd(self):
		return self._NewRcrd

	@NewRcrd.setter
	def NewRcrd(self, value):
		self._NewRcrd = value if type(value) != auto else self.make_default("NewRcrd")

	@NewRcrd.deleter
	def NewRcrd(self):
		del self._NewRcrd
		self._NewRcrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CancRcrd', type=SecuritiesReferenceDataReport7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TermntdRcrd', type=SecuritiesReferenceDataReport6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ModfdRcrd', type=SecuritiesReferenceDataReport6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NewRcrd', type=SecuritiesReferenceDataReport6, min=0, max=1, mutex_group=1, array=False),
	))

