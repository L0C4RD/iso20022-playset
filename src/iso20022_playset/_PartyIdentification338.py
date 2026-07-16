# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentification335Choice

class PartyIdentification338(base_types._BaseFieldType):

	__slots__ = ["_BlckgRef", "_LglPrsn"]
	@property
	def BlckgRef(self):
		return self._BlckgRef

	@BlckgRef.setter
	def BlckgRef(self, value):
		self._BlckgRef = value if value is not None else base_types.UninitialisedField(self, 'BlckgRef', Max35Text, False)

	@BlckgRef.deleter
	def BlckgRef(self):
		del self._BlckgRef
		self._BlckgRef = base_types.UninitialisedField(self, 'BlckgRef', Max35Text, False)

	@property
	def LglPrsn(self):
		return self._LglPrsn

	@LglPrsn.setter
	def LglPrsn(self, value):
		self._LglPrsn = value if value is not None else base_types.UninitialisedField(self, 'LglPrsn', PartyIdentification335Choice, False)

	@LglPrsn.deleter
	def LglPrsn(self):
		del self._LglPrsn
		self._LglPrsn = base_types.UninitialisedField(self, 'LglPrsn', PartyIdentification335Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckgRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglPrsn', type=PartyIdentification335Choice, min=0, max=1, mutex_group=None, array=False),
	))