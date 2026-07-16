# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalRightCode1Choice
from . import AdditionalRightThreshold2Choice
from . import DateFormat58Choice
from . import Max2048Text

class AdditionalRights4(base_types._BaseFieldType):

	__slots__ = ["_AddtlRght", "_AddtlRghtDdln", "_AddtlRghtInfURLAdr", "_AddtlRghtMktDdln", "_AddtlRghtThrshld"]
	@property
	def AddtlRght(self):
		return self._AddtlRght

	@AddtlRght.setter
	def AddtlRght(self, value):
		self._AddtlRght = value if value is not None else base_types.UninitialisedField(self, 'AddtlRght', AdditionalRightCode1Choice, False)

	@AddtlRght.deleter
	def AddtlRght(self):
		del self._AddtlRght
		self._AddtlRght = base_types.UninitialisedField(self, 'AddtlRght', AdditionalRightCode1Choice, False)

	@property
	def AddtlRghtDdln(self):
		return self._AddtlRghtDdln

	@AddtlRghtDdln.setter
	def AddtlRghtDdln(self, value):
		self._AddtlRghtDdln = value if value is not None else base_types.UninitialisedField(self, 'AddtlRghtDdln', DateFormat58Choice, False)

	@AddtlRghtDdln.deleter
	def AddtlRghtDdln(self):
		del self._AddtlRghtDdln
		self._AddtlRghtDdln = base_types.UninitialisedField(self, 'AddtlRghtDdln', DateFormat58Choice, False)

	@property
	def AddtlRghtInfURLAdr(self):
		return self._AddtlRghtInfURLAdr

	@AddtlRghtInfURLAdr.setter
	def AddtlRghtInfURLAdr(self, value):
		self._AddtlRghtInfURLAdr = value if value is not None else base_types.UninitialisedField(self, 'AddtlRghtInfURLAdr', Max2048Text, False)

	@AddtlRghtInfURLAdr.deleter
	def AddtlRghtInfURLAdr(self):
		del self._AddtlRghtInfURLAdr
		self._AddtlRghtInfURLAdr = base_types.UninitialisedField(self, 'AddtlRghtInfURLAdr', Max2048Text, False)

	@property
	def AddtlRghtMktDdln(self):
		return self._AddtlRghtMktDdln

	@AddtlRghtMktDdln.setter
	def AddtlRghtMktDdln(self, value):
		self._AddtlRghtMktDdln = value if value is not None else base_types.UninitialisedField(self, 'AddtlRghtMktDdln', DateFormat58Choice, False)

	@AddtlRghtMktDdln.deleter
	def AddtlRghtMktDdln(self):
		del self._AddtlRghtMktDdln
		self._AddtlRghtMktDdln = base_types.UninitialisedField(self, 'AddtlRghtMktDdln', DateFormat58Choice, False)

	@property
	def AddtlRghtThrshld(self):
		return self._AddtlRghtThrshld

	@AddtlRghtThrshld.setter
	def AddtlRghtThrshld(self, value):
		self._AddtlRghtThrshld = value if value is not None else base_types.UninitialisedField(self, 'AddtlRghtThrshld', AdditionalRightThreshold2Choice, False)

	@AddtlRghtThrshld.deleter
	def AddtlRghtThrshld(self):
		del self._AddtlRghtThrshld
		self._AddtlRghtThrshld = base_types.UninitialisedField(self, 'AddtlRghtThrshld', AdditionalRightThreshold2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRght', type=AdditionalRightCode1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRghtDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRghtInfURLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRghtMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRghtThrshld', type=AdditionalRightThreshold2Choice, min=0, max=1, mutex_group=None, array=False),
	))