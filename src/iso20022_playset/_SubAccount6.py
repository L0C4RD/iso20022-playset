# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text

class SubAccount6(base_types._BaseFieldType):

	__slots__ = ["_AcctDsgnt", "_Chrtc", "_Id", "_Nm"]
	@property
	def AcctDsgnt(self):
		return self._AcctDsgnt

	@AcctDsgnt.setter
	def AcctDsgnt(self, value):
		self._AcctDsgnt = value if type(value) != base_types.auto else self.make_default("AcctDsgnt")

	@AcctDsgnt.deleter
	def AcctDsgnt(self):
		del self._AcctDsgnt
		self._AcctDsgnt = None

	@property
	def Chrtc(self):
		return self._Chrtc

	@Chrtc.setter
	def Chrtc(self, value):
		self._Chrtc = value if type(value) != base_types.auto else self.make_default("Chrtc")

	@Chrtc.deleter
	def Chrtc(self):
		del self._Chrtc
		self._Chrtc = None

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

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrtc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))