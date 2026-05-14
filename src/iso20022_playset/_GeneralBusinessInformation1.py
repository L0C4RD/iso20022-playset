# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InformationQualifierType1 import InformationQualifierType1
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text

class GeneralBusinessInformation1(base_types._BaseFieldType):

	__slots__ = ["_Qlfr", "_Sbjt", "_SbjtDtls"]
	@property
	def Qlfr(self):
		return self._Qlfr

	@Qlfr.setter
	def Qlfr(self, value):
		self._Qlfr = value if type(value) != base_types.auto else self.make_default("Qlfr")

	@Qlfr.deleter
	def Qlfr(self):
		del self._Qlfr
		self._Qlfr = None

	@property
	def Sbjt(self):
		return self._Sbjt

	@Sbjt.setter
	def Sbjt(self, value):
		self._Sbjt = value if type(value) != base_types.auto else self.make_default("Sbjt")

	@Sbjt.deleter
	def Sbjt(self):
		del self._Sbjt
		self._Sbjt = None

	@property
	def SbjtDtls(self):
		return self._SbjtDtls

	@SbjtDtls.setter
	def SbjtDtls(self, value):
		self._SbjtDtls = value if type(value) != base_types.auto else self.make_default("SbjtDtls")

	@SbjtDtls.deleter
	def SbjtDtls(self):
		del self._SbjtDtls
		self._SbjtDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qlfr', type=InformationQualifierType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sbjt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))