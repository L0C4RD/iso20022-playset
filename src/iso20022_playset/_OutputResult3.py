# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InformationQualify1Code
from . import ResponseType11
from . import UserInterface9Code

class OutputResult3(base_types._BaseFieldType):

	__slots__ = ["_DvcTp", "_InfQlfr", "_Rspn"]
	@property
	def DvcTp(self):
		return self._DvcTp

	@DvcTp.setter
	def DvcTp(self, value):
		self._DvcTp = value if value is not None else base_types.UninitialisedField(self, 'DvcTp', UserInterface9Code, False)

	@DvcTp.deleter
	def DvcTp(self):
		del self._DvcTp
		self._DvcTp = base_types.UninitialisedField(self, 'DvcTp', UserInterface9Code, False)

	@property
	def InfQlfr(self):
		return self._InfQlfr

	@InfQlfr.setter
	def InfQlfr(self, value):
		self._InfQlfr = value if value is not None else base_types.UninitialisedField(self, 'InfQlfr', InformationQualify1Code, False)

	@InfQlfr.deleter
	def InfQlfr(self):
		del self._InfQlfr
		self._InfQlfr = base_types.UninitialisedField(self, 'InfQlfr', InformationQualify1Code, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DvcTp', type=UserInterface9Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfQlfr', type=InformationQualify1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
	))