# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text
from ._Party50Choice import Party50Choice

class CaseAssignment6(base_types._BaseFieldType):

	__slots__ = ["_Assgne", "_Assgnr", "_CreDtTm", "_Id"]
	@property
	def Assgne(self):
		return self._Assgne

	@Assgne.setter
	def Assgne(self, value):
		self._Assgne = value if type(value) != base_types.auto else self.make_default("Assgne")

	@Assgne.deleter
	def Assgne(self):
		del self._Assgne
		self._Assgne = None

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != base_types.auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgne', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))