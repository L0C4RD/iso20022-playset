# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DocumentLineInformation1 import DocumentLineInformation1
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._ReferredDocumentType4 import ReferredDocumentType4

class ReferredDocumentInformation7(base_types._BaseFieldType):

	__slots__ = ["_LineDtls", "_Nb", "_RltdDt", "_Tp"]
	@property
	def LineDtls(self):
		return self._LineDtls

	@LineDtls.setter
	def LineDtls(self, value):
		self._LineDtls = value if type(value) != base_types.auto else self.make_default("LineDtls")

	@LineDtls.deleter
	def LineDtls(self):
		del self._LineDtls
		self._LineDtls = None

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != base_types.auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def RltdDt(self):
		return self._RltdDt

	@RltdDt.setter
	def RltdDt(self, value):
		self._RltdDt = value if type(value) != base_types.auto else self.make_default("RltdDt")

	@RltdDt.deleter
	def RltdDt(self):
		del self._RltdDt
		self._RltdDt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='LineDtls', type=DocumentLineInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReferredDocumentType4, min=0, max=1, mutex_group=None, array=False),
	))