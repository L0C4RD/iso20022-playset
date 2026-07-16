# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentLineInformation1
from . import ISODate
from . import Max35Text
from . import ReferredDocumentType4

class ReferredDocumentInformation7(base_types._BaseFieldType):

	__slots__ = ["_LineDtls", "_Nb", "_RltdDt", "_Tp"]
	@property
	def LineDtls(self):
		return self._LineDtls

	@LineDtls.setter
	def LineDtls(self, value):
		self._LineDtls = value if value is not None else base_types.UninitialisedField(self, 'LineDtls', DocumentLineInformation1, True)

	@LineDtls.deleter
	def LineDtls(self):
		del self._LineDtls
		self._LineDtls = base_types.UninitialisedField(self, 'LineDtls', DocumentLineInformation1, True)

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@property
	def RltdDt(self):
		return self._RltdDt

	@RltdDt.setter
	def RltdDt(self, value):
		self._RltdDt = value if value is not None else base_types.UninitialisedField(self, 'RltdDt', ISODate, False)

	@RltdDt.deleter
	def RltdDt(self):
		del self._RltdDt
		self._RltdDt = base_types.UninitialisedField(self, 'RltdDt', ISODate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ReferredDocumentType4, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ReferredDocumentType4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LineDtls', type=DocumentLineInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReferredDocumentType4, min=0, max=1, mutex_group=None, array=False),
	))