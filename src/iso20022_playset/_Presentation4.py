# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Document11 import Document11
from ._Max2000Text import Max2000Text
from ._PresentationMedium1Choice import PresentationMedium1Choice

class Presentation4(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Doc", "_Mdm"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Doc(self):
		return self._Doc

	@Doc.setter
	def Doc(self, value):
		self._Doc = value if type(value) != base_types.auto else self.make_default("Doc")

	@Doc.deleter
	def Doc(self):
		del self._Doc
		self._Doc = None

	@property
	def Mdm(self):
		return self._Mdm

	@Mdm.setter
	def Mdm(self, value):
		self._Mdm = value if type(value) != base_types.auto else self.make_default("Mdm")

	@Mdm.deleter
	def Mdm(self):
		del self._Mdm
		self._Mdm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Doc', type=Document11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mdm', type=PresentationMedium1Choice, min=0, max=1, mutex_group=None, array=False),
	))