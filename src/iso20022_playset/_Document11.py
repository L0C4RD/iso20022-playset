from . import base_types
from ._Max20000Text import Max20000Text
from ._PresentationDocumentFormat1Choice import PresentationDocumentFormat1Choice
from ._Presentation3 import Presentation3

class Document11(base_types._BaseFieldType):

	__slots__ = ["_Wrdg", "_Tp", "_ElctrncDtls"]
	@property
	def Wrdg(self):
		return self._Wrdg

	@Wrdg.setter
	def Wrdg(self, value):
		self._Wrdg = value if type(value) != base_types.auto else self.make_default("Wrdg")

	@Wrdg.deleter
	def Wrdg(self):
		del self._Wrdg
		self._Wrdg = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def ElctrncDtls(self):
		return self._ElctrncDtls

	@ElctrncDtls.setter
	def ElctrncDtls(self, value):
		self._ElctrncDtls = value if type(value) != base_types.auto else self.make_default("ElctrncDtls")

	@ElctrncDtls.deleter
	def ElctrncDtls(self):
		del self._ElctrncDtls
		self._ElctrncDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Wrdg', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PresentationDocumentFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncDtls', type=Presentation3, min=0, max=None, mutex_group=None, array=True),
	))

