from . import base_types
from ._AdviceType1Choice import AdviceType1Choice

class AdviceType1(base_types._BaseFieldType):

	__slots__ = ["_DbtAdvc", "_CdtAdvc"]
	@property
	def DbtAdvc(self):
		return self._DbtAdvc

	@DbtAdvc.setter
	def DbtAdvc(self, value):
		self._DbtAdvc = value if type(value) != base_types.auto else self.make_default("DbtAdvc")

	@DbtAdvc.deleter
	def DbtAdvc(self):
		del self._DbtAdvc
		self._DbtAdvc = None

	@property
	def CdtAdvc(self):
		return self._CdtAdvc

	@CdtAdvc.setter
	def CdtAdvc(self, value):
		self._CdtAdvc = value if type(value) != base_types.auto else self.make_default("CdtAdvc")

	@CdtAdvc.deleter
	def CdtAdvc(self):
		del self._CdtAdvc
		self._CdtAdvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DbtAdvc', type=AdviceType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtAdvc', type=AdviceType1Choice, min=0, max=1, mutex_group=None, array=False),
	))

