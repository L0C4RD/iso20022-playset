from . import base_types
from .SecuritiesOption86 import SecuritiesOption86
from .CorporateActionOption39Choice import CorporateActionOption39Choice
from .OptionNumber1Choice import OptionNumber1Choice
from .CashOption112 import CashOption112

class CorporateActionOption246(base_types._BaseFieldType):

	__slots__ = ["_OptnNb", "_CshMvmntDtls", "_SctiesMvmntDtls", "_OptnTp"]
	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != base_types.auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if type(value) != base_types.auto else self.make_default("CshMvmntDtls")

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = None

	@property
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if type(value) != base_types.auto else self.make_default("SctiesMvmntDtls")

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OptnNb', type=OptionNumber1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmntDtls', type=CashOption112, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=SecuritiesOption86, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption39Choice, min=1, max=1, mutex_group=None, array=False),
	))

