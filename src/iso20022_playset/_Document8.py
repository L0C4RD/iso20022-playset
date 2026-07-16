# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max20000Text
from . import Presentation3
from . import PresentationDocumentFormat1Choice

class Document8(base_types._BaseFieldType):

	__slots__ = ["_ElctrncDtls", "_Tp", "_Wrdg"]
	@property
	def ElctrncDtls(self):
		return self._ElctrncDtls

	@ElctrncDtls.setter
	def ElctrncDtls(self, value):
		self._ElctrncDtls = value if value is not None else base_types.UninitialisedField(self, 'ElctrncDtls', Presentation3, True)

	@ElctrncDtls.deleter
	def ElctrncDtls(self):
		del self._ElctrncDtls
		self._ElctrncDtls = base_types.UninitialisedField(self, 'ElctrncDtls', Presentation3, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', PresentationDocumentFormat1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', PresentationDocumentFormat1Choice, False)

	@property
	def Wrdg(self):
		return self._Wrdg

	@Wrdg.setter
	def Wrdg(self, value):
		self._Wrdg = value if value is not None else base_types.UninitialisedField(self, 'Wrdg', Max20000Text, False)

	@Wrdg.deleter
	def Wrdg(self):
		del self._Wrdg
		self._Wrdg = base_types.UninitialisedField(self, 'Wrdg', Max20000Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElctrncDtls', type=Presentation3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=PresentationDocumentFormat1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wrdg', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
	))