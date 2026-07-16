# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Document11
from . import Max2000Text
from . import PresentationMedium1Choice

class Presentation4(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Doc", "_Mdm"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def Doc(self):
		return self._Doc

	@Doc.setter
	def Doc(self, value):
		self._Doc = value if value is not None else base_types.UninitialisedField(self, 'Doc', Document11, True)

	@Doc.deleter
	def Doc(self):
		del self._Doc
		self._Doc = base_types.UninitialisedField(self, 'Doc', Document11, True)

	@property
	def Mdm(self):
		return self._Mdm

	@Mdm.setter
	def Mdm(self, value):
		self._Mdm = value if value is not None else base_types.UninitialisedField(self, 'Mdm', PresentationMedium1Choice, False)

	@Mdm.deleter
	def Mdm(self):
		del self._Mdm
		self._Mdm = base_types.UninitialisedField(self, 'Mdm', PresentationMedium1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Doc', type=Document11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mdm', type=PresentationMedium1Choice, min=0, max=1, mutex_group=None, array=False),
	))